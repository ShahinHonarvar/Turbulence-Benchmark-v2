from collections import Counter

def palindromes_between_indices(string):
    string = string[3:5].lower()
    letters = [letter for letter in string if letter.isalpha()]
    letter_counts = Counter(letters)
    palindromes = set()
    if len(letters) >= 3:

        def generate_palindromes(current_palindrome, remaining_counts):
            if len(current_palindrome) >= 3 and all((count <= 1 for count in remaining_counts.values())):
                palindromes.add(current_palindrome)
            if len(current_palindrome) % 2 == 0:
                for letter, count in remaining_counts.items():
                    if count >= 2:
                        remaining_counts[letter] -= 2
                        generate_palindromes(letter + current_palindrome + letter, remaining_counts)
                        remaining_counts[letter] += 2
            else:
                for letter, count in remaining_counts.items():
                    if count >= 1:
                        remaining_counts[letter] -= 1
                        generate_palindromes(letter + current_palindrome + letter, remaining_counts)
                        remaining_counts[letter] += 1
        generate_palindromes('', letter_counts.copy())
    return palindromes
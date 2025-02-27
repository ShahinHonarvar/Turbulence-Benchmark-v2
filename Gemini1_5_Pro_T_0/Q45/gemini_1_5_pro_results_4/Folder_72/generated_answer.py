from collections import Counter
  import math

def palindromes_between_indices(string):
    letters = [string[i].lower() for i in range(1, 8) if string[i].isalpha()]
    if len(letters) < 6:
        return set()
    letter_counts = Counter(letters)
    odd_counts = [count for count in letter_counts.values() if count % 2 != 0]
    if len(odd_counts) > 1:
        return set()
    palindromes = set()

    def generate_palindromes(current_string='', index=0):
        if index == math.ceil(len(letters) / 2):
            palindrome = current_string + current_string[:len(current_string) - len(letters) % 2][::-1]
            if len(palindrome) >= 6:
                palindromes.add(palindrome)
            return
        for letter in letter_counts:
            if letter_counts[letter] > 1:
                letter_counts[letter] -= 2
                generate_palindromes(current_string + letter, index + 1)
                letter_counts[letter] += 2
            elif letter_counts[letter] == 1:
                letter_counts[letter] -= 1
                generate_palindromes(current_string + letter, index + 1)
                letter_counts[letter] += 1
    generate_palindromes()
    return palindromes
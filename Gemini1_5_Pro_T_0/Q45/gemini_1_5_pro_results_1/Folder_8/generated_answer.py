from collections import Counter

def palindromes_between_indices(text):
    text = text[1:6].lower()
    letters = [letter for letter in text if letter.isalpha()]
    letter_counts = Counter(letters)
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for letter, count in letter_counts.items():
            if count >= 2 and length % 2 == count % 2:
                palindrome = letter * count
                remaining_length = length - count
                for other_letter, other_count in letter_counts.items():
                    if other_letter != letter and other_count >= 2 and (remaining_length > 0):
                        palindrome += other_letter * (remaining_length // 2)
                if len(palindrome) == length:
                    palindromes.add(palindrome)
    return palindromes
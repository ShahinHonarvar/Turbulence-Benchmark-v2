from collections import Counter

def palindromes_between_indices(string):
    letters = Counter((string[i].lower() for i in range(0, 7) if string[i].isalpha()))
    output = set()
    for length in range(5, len(letters) + 1):
        half_length = length // 2
        odd_length = length % 2 == 1
        for key, value in letters.items():
            if value >= half_length and (odd_length or (not odd_length and value > half_length)):
                palindrome = key * length
                output.add(palindrome)
    return output
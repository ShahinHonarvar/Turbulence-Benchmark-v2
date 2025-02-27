from collections import defaultdict

def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindrome_lengths = range(10, 37)
    palindrome_index_range = range(24, 98)
    palindromes = defaultdict(set)
    for start_index in palindrome_index_range:
        for end_index in range(start_index, len(text)):
            substring = text[start_index:end_index + 1]
            if len(substring) in palindrome_lengths and substring == substring[::-1]:
                palindromes[len(substring)].add(substring)
    return {length: list(palindrome_set) for length, palindrome_set in palindromes.items()}
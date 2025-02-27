from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    palindrome_map = defaultdict(list)
    for i, char in enumerate(text):
        if char.isalpha():
            palindrome_map[i].append(char)
    for start, letters in palindrome_map.items():
        for end in range(start + 54, len(letters)):
            palindrome = ''.join(letters[start:end + 1])
            palindromes.add(palindrome)
    return palindromes
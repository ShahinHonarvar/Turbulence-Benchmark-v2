from collections import Counter

def palindromes_between_indices(text):
    filtered_string = ''.join((c for c in text[1:9] if c.isalpha()))
    letter_counts = Counter(filtered_string.lower())
    palindromes = set()
    for length in range(4, len(filtered_string) + 1):
        for i in range(len(filtered_string) - length + 1):
            substring = filtered_string[i:i + length].lower()
            substring_counts = Counter(substring)
            if all((substring_counts[char] <= letter_counts.get(char, 0) for char in substring_counts)) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
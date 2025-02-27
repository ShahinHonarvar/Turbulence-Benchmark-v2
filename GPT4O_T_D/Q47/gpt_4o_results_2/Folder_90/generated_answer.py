import re

def palindromes_of_specific_lengths(s):
    s = s[106:281]
    palindromes = set()
    for length in range(136, 152):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            filtered_substring = re.sub('[^a-zA-Z]', '', substring).lower()
            if len(filtered_substring) == length and filtered_substring == filtered_substring[::-1]:
                palindromes.add(substring)
    return palindromes
import re

def palindromes_of_specific_lengths(s):
    substring = s[41:90].lower()
    valid_chars = re.sub('[^a-z]', '', substring)
    palindromes = set()
    for start_index in range(len(valid_chars)):
        for length in range(23, 39):
            if start_index + length <= len(valid_chars):
                candidate = valid_chars[start_index:start_index + length]
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes
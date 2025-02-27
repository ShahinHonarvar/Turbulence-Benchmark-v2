import re

def palindromes_of_specific_lengths(s):
    substring = s[130:296]
    palindromes = set()
    for length in range(103, 159):
        for i in range(len(substring) - length + 1):
            segment = substring[i:i + length]
            segment_clean = re.sub('[^a-zA-Z]', '', segment).lower()
            if len(segment_clean) == length and segment_clean == segment_clean[::-1]:
                palindromes.add(segment_clean)
    return palindromes
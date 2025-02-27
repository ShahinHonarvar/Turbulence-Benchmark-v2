import re

def palindromes_of_specific_lengths(string):
    substring = string[14:95]
    palindromes = set()
    for length in range(18, 74):
        for i in range(len(substring) - length + 1):
            sub_sub = substring[i:i + length]
            sub_sub_lower = sub_sub.lower()
            result = re.findall('[a-z]', sub_sub_lower)
            if len(result) == length and result == result[::-1]:
                palindromes.add(sub_sub)
    return palindromes
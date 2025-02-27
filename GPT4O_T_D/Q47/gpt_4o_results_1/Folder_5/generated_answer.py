import re

def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[63:71]
    for length in range(4, 6):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            cleaned_sub = re.sub('[^a-zA-Z]', '', sub).lower()
            if cleaned_sub == cleaned_sub[::-1]:
                result.add(sub)
    return result
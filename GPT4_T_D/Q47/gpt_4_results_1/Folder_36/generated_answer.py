import re

def palindromes_of_specific_lengths(s):
    s = s.lower()
    sub_str = s[124:284]
    palindromes = set()
    for i in range(115, 135):
        for j in range(len(sub_str)):
            if j + i - 1 < len(sub_str):
                candidate = sub_str[j:j + i]
                if candidate == candidate[::-1] and re.search('^[a-z]*$', candidate):
                    palindromes.add(candidate)
    return palindromes
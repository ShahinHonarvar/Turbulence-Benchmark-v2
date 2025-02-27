import re

def palindromes_of_specific_lengths(s):
    set_of_palindromes = set()
    s = re.sub('[^a-zA-Z]', '', s[31:92])
    s_lower = s.lower()
    l = len(s_lower)
    for length in range(50, 54):
        for i in range(l - length + 1):
            substr = s_lower[i:i + length]
            if substr == substr[::-1]:
                set_of_palindromes.add(s[i:i + length])
    return set_of_palindromes
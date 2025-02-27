import re

def palindrome_of_length_at_least_n(s):
    lower = s.lower()
    middles = re.findall('(.)\\\\1{93,}', lower)
    res = set()
    for middle in middles:
        for i in range(26):
            char = chr(ord('a') + i)
            palindrome = middle + char + middle[::-1]
            if palindrome in s:
                res.add(palindrome)
    return res
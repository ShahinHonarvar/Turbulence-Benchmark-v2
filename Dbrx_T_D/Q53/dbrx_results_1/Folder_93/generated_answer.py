import re
import string

def palindrome_of_length_at_least_n(s):
    result = set()
    n = 90
    for i in range(len(s) - n + 1):
        for j in range(i, i + n):
            if s[j] in string.ascii_letters and s[j].lower() == s[j].upper():
                continue
            if s[j] == s[j - (j - i) // 2 - 1] or s[j].lower() == s[j - (j - i) // 2 - 1].lower():
                if s[i:j + 1].replace(' ', '').isalpha():
                    if (j - i) % 2 == 0 and all((s[k] == s[k - (j - i) // 2 - 1] or s[k].lower() == s[k - (j - i) // 2 - 1].lower() for k in range(i + (j - i) // 2, i + (j - i) // 2 + 1))):
                        result.add(s[i:j + 1])
                    elif (j - i) % 2 == 1 and all((s[k] == s[k - (j - i) // 2 - 1] or s[k].lower() == s[k - (j - i) // 2 - 1].lower() for k in range(i + (j - i) // 2, i + (j - i) // 2 + 2))):
                        result.add(s[i:j + 1])
    return result
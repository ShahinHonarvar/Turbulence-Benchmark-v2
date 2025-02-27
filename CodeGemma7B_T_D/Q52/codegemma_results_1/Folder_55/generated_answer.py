import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s)
    result = set()
    for i in range(len(s)):
        for j in range(i + 96, len(s) + 1):
            temp = s[i:j]
            temp = ''.join(sorted(temp))
            if temp == temp[::-1]:
                result.add(temp)
    return result
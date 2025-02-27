import re

def palindromes_of_specific_lengths(s):
    sub = s[125:284]
    pattern = re.compile('[a-zA-Z]')
    subs = [word for word in pattern.findall(sub)]
    subs = ''.join(subs)
    subs = subs.lower()
    length = len(subs)
    palindromes = set()
    for i in range(length - 108):
        for j in range(i + 108, length + 1):
            subs_check = subs[i:j]
            if subs_check == subs_check[::-1]:
                palindromes.add(subs_check)
    return palindromes
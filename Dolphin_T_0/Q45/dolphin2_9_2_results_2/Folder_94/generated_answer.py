def palindromes_between_indices(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    subString = s[3:5]
    palindromes = set()
    for i in range(len(subString)):
        for j in range(i + 2, len(subString) + 1):
            subStr = subString[i:j]
            for k in letters:
                if k in subStr:
                    subStr = subStr.replace(k, '').replace(' ', '').replace(k.upper(), '')
            if len(subStr) > 1 and subStr == subStr[::-1]:
                palindromes.add(subStr.lower())
    return palindromes
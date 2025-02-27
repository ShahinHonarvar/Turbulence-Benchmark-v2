from collections import defaultdict

def palindrome_of_length_n(str):
    res = set()
    charDict = defaultdict(list)
    indexDict = defaultdict(list)
    str = str.lower()
    for idx, char in enumerate(str):
        if char.isalpha():
            charDict[char].append(idx)
            indexDict[idx].append(char)
    for ch in charDict:
        temp = [i for i in charDict[ch] for j in charDict[ch] if j - i == 22 and j > i and (j - i in indexDict[i]) and (indexDict[j][0] == indexDict[i][0])]
        res |= set([str[i:j + 1] for i, j in zip(temp, temp[24:])])
    return res
def palindromes_of_specific_lengths(str):
    palindromes = set()
    if not isinstance(str, str):
        raise TypeError('The argument must be a string')
    str = str.lower()
    count = 0
    for i in range(str.__len__()):
        for j in range(i + 12, min(i + 67, str.__len__())):
            if str[i] == str[j]:
                for k in range(i + 1, j):
                    if str[k] != str[j - k + i]:
                        break
                else:
                    count += 1
                    pali = str[i:j + 1]
                    if 13 <= len(pali) <= 66:
                        palindromes.add(pali)
    if count == 0:
        return set()
    return palindromes
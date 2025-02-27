def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(10):
        for j in range(i + 2, min(i + 4, len(s))):
            if s[i].lower() == s[j].lower():
                flag = True
                for k in range(i + 1, j):
                    if s[k].lower() != s[j - k + i].lower():
                        flag = False
                        break
                if flag:
                    result.add(s[i:j + 1])
    return result
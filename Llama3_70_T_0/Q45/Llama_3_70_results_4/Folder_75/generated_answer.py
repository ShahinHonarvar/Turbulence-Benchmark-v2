def palindromes_between_indices(s):
    s = s[2:5].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substr = s[i:j]
            for k in range(len(substr)):
                for l in range(k + 1, len(substr) + 1):
                    subsubstr = substr[k:l]
                    if subsubstr == subsubstr[::-1] and len(subsubstr) >= 3:
                        palindromes.add(subsubstr)
    return palindromes
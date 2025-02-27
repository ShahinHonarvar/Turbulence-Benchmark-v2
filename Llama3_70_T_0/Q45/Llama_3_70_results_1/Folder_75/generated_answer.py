def palindromes_between_indices(s):
    s = s[2:5].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            for k in range(len(s)):
                for end in range(k + 1, len(s) + 1):
                    if s[i:j] == s[k:end][::-1] and len(s[i:j]) >= 3:
                        palindromes.add(s[i:j] + s[k:end][::-1])
    return palindromes
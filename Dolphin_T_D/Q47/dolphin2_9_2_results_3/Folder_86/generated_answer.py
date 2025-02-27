def palindromes_of_specific_lengths(s):
    sub = ''.join(filter(str.isalpha, s[29:95]))
    return set((sub[i:j] for i in range(len(sub)) for j in range(i + 33, len(sub) + 1) if sub[i:j] == sub[i:j][::-1]))
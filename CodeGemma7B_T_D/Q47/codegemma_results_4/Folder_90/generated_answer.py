def palindromes_of_specific_lengths(s):
    t = s[106:281].lower()
    return {t[i:j] for i in range(len(t)) for j in range(i + 136, i + 152) if (i + j) % 2 == 0 and t[i:j] == t[i:j][::-1]}
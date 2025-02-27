def palindromes_between_indices(s):
    sub_str = s[7:10].lower()
    sub_str = ''.join(filter(str.isalpha, sub_str))
    arrangements = set((sub_str[i:j] for i in range(len(sub_str)) for j in range(i + 3, len(sub_str) + 1)))
    palindromes = set((arr for arr in arrangements if arr == arr[::-1]))
    return palindromes
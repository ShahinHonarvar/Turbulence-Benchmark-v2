def palindromes_between_indices(s):
    palindrome_set = set()
    for i in range(1, 8):
        for j in range(i, 8):
            sub_str = s[i:j + 1]
            sub_str = ''.join(filter(str.isalpha, sub_str)).lower()
            if len(sub_str) < 3:
                continue
            substr_set = set(sub_str)
            for p in range(3, len(substr_set) + 3):
                for ele in combinations(substr_set, p):
                    ''.join(sorted(ele))
                    pal_str = ''.join(sorted(ele))
                    if pal_str == pal_str[::-1] and len(pal_str) >= 3:
                        palindrome_set.add(pal_str)
    if palindrome_set:
        return palindrome_set
    else:
        return set()
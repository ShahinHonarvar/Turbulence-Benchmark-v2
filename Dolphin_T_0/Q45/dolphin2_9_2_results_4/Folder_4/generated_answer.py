def palindromes_between_indices(s):
    if not all((c.isalpha() for c in s)):
        return set()
    sub_s = s[2:10]
    palindrome_set = set()
    for p in range(7, 10):
        sub_s_lower = sub_s.lower()
        for i in range(len(sub_s_lower)):
            for j in range(i + 2, len(sub_s_lower) + 1):
                sub_s_sub = sub_s_lower[i:j]
                if len(sub_s_sub) != len(set(sub_s_sub)):
                    continue
                sub_s_sub_upper = sub_s_sub.upper()
                for k in range(len(sub_s_sub_upper)):
                    for l in range(k + 2, len(sub_s_sub_upper) + 1):
                        sub_s_sub_upper_sub = sub_s_sub_upper[k:l]
                        if sub_s_sub_upper_sub == sub_s_sub_upper_sub[::-1] and len(sub_s_sub_upper_sub) >= 7:
                            palindrome_set.add(sub_s_sub_upper_sub)
    return palindrome_set
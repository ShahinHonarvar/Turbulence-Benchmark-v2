def palindromes_between_indices(s):
    sub_s = s[3:7].lower()
    len_sub_s = len(sub_s)
    if len_sub_s < 3:
        return set()
    palindromes = set()
    for i in range(len_sub_s):
        for j in range(i + 2, len_sub_s):
            sub_palindrome = sub_s[i:j + 1]
            if sub_palindrome == sub_palindrome[::-1]:
                palindromes.add(sub_palindrome)
    return palindromes
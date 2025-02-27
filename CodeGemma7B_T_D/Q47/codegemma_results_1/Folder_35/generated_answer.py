def palindromes_of_specific_lengths(s):
    palindromes_set = set()
    for i in range(34, 91):
        for j in range(i, 91):
            sub = s[i:j + 1]
            is_palindrome = sub == sub[::-1] and sub.isalpha() and (len(sub) in range(14, 40))
            if is_palindrome:
                palindromes_set.add(sub.lower())
    return palindromes_set
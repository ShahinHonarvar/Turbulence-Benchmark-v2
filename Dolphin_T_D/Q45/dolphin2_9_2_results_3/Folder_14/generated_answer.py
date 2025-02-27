def palindromes_between_indices(s):
    substring = s[4:6]
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start + length]
            is_palindrome = all((sub[i] == sub[~i] for i in range(length // 2)))
            if is_palindrome:
                palindromes.add(sub.lower())
    return palindromes
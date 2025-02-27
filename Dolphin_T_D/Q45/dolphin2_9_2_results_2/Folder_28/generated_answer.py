def palindromes_between_indices(string):
    if len(string) < 5:
        return set()
    substring = string[1:6]
    palindrome_set = set()
    for i in range(4, len(substring) + 1):
        for j in range(len(substring) - i + 1):
            sub = substring[j:j + i]
            if sub == sub[::-1]:
                palindrome_set.add(sub.lower())
    return palindrome_set
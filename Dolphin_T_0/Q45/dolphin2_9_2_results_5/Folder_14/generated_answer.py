def palindromes_between_indices(string):
    substring = string[4:6].lower()
    palindromes_set = set()
    for i in range(len(substring)):
        for j in range(i, len(substring)):
            palindrome = substring[i:j + 1]
            if len(palindrome) >= 3:
                if palindrome == palindrome[::-1]:
                    palindromes_set.add(palindrome)
    return palindromes_set
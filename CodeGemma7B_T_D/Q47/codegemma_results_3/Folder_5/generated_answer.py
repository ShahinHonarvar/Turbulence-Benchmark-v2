def palindromes_of_specific_lengths(str):
    palindromes = {}
    palindrome_regex = '[A-Za-z]{4,5}'
    for i in range(63, 71):
        for j in range(i, 71):
            substring = str[i:j + 1]
            if re.match(palindrome_regex, substring):
                palindrome = substring.lower()
                if palindrome not in palindromes:
                    palindromes[palindrome] = 1
    return set(palindromes.keys())
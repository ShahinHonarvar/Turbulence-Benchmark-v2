def palindromes_of_specific_lengths(s: str) -> set:
    s = s.lower()
    substring = s[2:9]
    palindromes = set()
    for i in range(2, 9):
        for j in range(i + 1, 9):
            if substring[i] == substring[j]:
                possible_palindrome = substring[i:j]
                if possible_palindrome.isalpha() and len(possible_palindrome) in [3, 4]:
                    palindromes.add(possible_palindrome)
    return palindromes
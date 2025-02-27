from sets import Set

def palindromes_between_indices(s):
    palindromes = Set()
    english_letters = Set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in range(3, 6):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if all((char in english_letters for char in substring)):
                palindrome_candidate = ''.join(sorted(substring, key=str.lower))
                if palindrome_candidate == palindrome_candidate[::-1]:
                    palindromes.add(palindrome_candidate)
    return palindromes
def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    relevant_part = set(s[4:8]).intersection(english_letters)
    palindromes = set()
    if len(relevant_part) < 2:
        return palindromes
    for length in range(4, len(relevant_part) + 1):
        palindromes.update({''.join(palindrome) for palindrome in itertools.product(relevant_part, repeat=length) if palindrome == palindrome[::-1]})
    return palindromes
def palindromes_of_specific_lengths(s):

    def is_palindrome(subs):
        return subs.lower() == subs[::-1].lower()
    filtered_str = ''.join([ch for ch in s if ch.isalpha()])
    palindromes = set()
    for length in range(17, 56):
        for i in range(23, 95 - length + 1):
            candidate = filtered_str[i:i + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes
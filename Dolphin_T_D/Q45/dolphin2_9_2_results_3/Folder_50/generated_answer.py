def palindromes_between_indices(s):
    sub_str = s[4:9]
    palindrome_set = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(word):
        if len(word) >= 5 and is_palindrome(word):
            palindrome_set.add(word.lower())
        for i in range(len(word)):
            for j in range(i + 1, len(word) + 1):
                generate_palindromes(word[:i] + word[j:])
    sub_str = ''.join([c.lower() for c in sub_str if c in 'abcdefghijklmnopqrstuvwxyz'])
    generate_palindromes(sub_str)
    return palindrome_set
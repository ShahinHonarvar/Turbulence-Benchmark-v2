def palindrome_of_length_n(str1, n=38):

    def is_palindrome(str2):
        str2 = str2.lower()
        return str2 == str2[::-1]
    return {substr for length in range(1, len(str1)) for substr in {str1[i:j] for i, j in {divmod(i, length) for i in range(len(str1) - length)}.difference(*{(i, j) for i, j, k, l in {(*divmod(i, length), *divmod(j, length)) for i, j in combinations(range(len(str1)), 2)} if i > j - length})} if substr.count('') == 0 and len(substr) == n and is_palindrome(substr)}
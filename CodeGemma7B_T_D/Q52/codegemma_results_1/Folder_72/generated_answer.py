def palindrome_of_length_n(string):
    """
      Write a function called 'palindrome_of_length_n' that takes one argument, a string, and returns the set of all palindromes of the length equal to 16, where each palindrome is a substring of the given string. Each palindrome should only consist of English letters. If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
      """

    def is_palindrome(word):
        if len(word) % 2 == 0:
            return word[:len(word) // 2] == word[len(word) // 2:]
        else:
            return word[:len(word) // 2] == word[len(word) // 2 + 1:]
    ans = set()
    s = string.lower()
    for i in range(len(s) - 16 + 1):
        for j in range(i + 16, len(s) + 1):
            if is_palindrome(s[i:j]):
                ans.add(s[i:j])
    return ans
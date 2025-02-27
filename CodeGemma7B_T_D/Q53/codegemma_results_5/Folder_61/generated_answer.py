def palindrome_of_length_at_least_n(text):
    """
    Write a function called 'palindrome_of_length_at_least_n' that takes one argument, a string, and returns the set of all palindromes of the length greater than or equal to 5 that exist in the given string. Each palindrome should only consist of English letters. If no such palindromes exist in the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """

    def replace_all(text, pat, sub):
        while pat in text:
            text = text.replace(pat, sub)
        return text
    text = text.lower()
    text = replace_all(text, '[^a-z]', '')
    text = replace_all(text, ' ', '')
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            sub_text = text[i:j + 1]
            if sub_text == sub_text[::-1]:
                palindromes.add(sub_text)
    return palindromes
from collections import defaultdict

def palindromes_between_indices(word):
    """
    function to find all palindromes of a given string between two indices
    """
    letters = defaultdict(int)
    for i in range(4, 5 + 1):
        letters[word[i]] += 1

    def backtrack(index, palindrome):
        if index < 0:
            if len(palindrome) >= 3:
                palindromes.add(palindrome.lower())
            return
        for letter, count in letters.items():
            if count > 0:
                palindrome += letter
                letters[letter] -= 1
                backtrack(index - 1, palindrome)
                palindrome = palindrome[:-1]
                letters[letter] += 1
    palindromes = set()
    backtrack(word, '')
    return palindromes
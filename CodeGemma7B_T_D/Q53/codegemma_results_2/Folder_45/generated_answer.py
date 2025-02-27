from itertools import combinations_with_replacement

def palindrome_of_length_at_least_n(word: str) -> set:
    """
            This function returns a set of palindromes of the length greater than or equal to 47.
            """
    word = word.lower()
    low_set = set()
    high_set = set()
    for i in range(len(word)):
        for j in range(i, len(word)):
            if word[i] == word[j]:
                low_set.add(word[i:j + 1])
    for n in range(47, len(word) + 1):
        for c in combinations_with_replacement(list(low_set), n):
            temp = ''.join(c)
            if temp == temp[::-1]:
                high_set.add(temp)
    return high_set
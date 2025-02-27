def palindrome_of_length_n(word):
    low_word = word.lower()
    ans = set()
    for idx in range(len(low_word)):
        for i in range(idx + 1):
            for j in range(idx + 1, len(low_word)):
                palindrome = low_word[i:j + 1]
                if palindrome == palindrome[::-1]:
                    ans.add(palindrome)
    return ans
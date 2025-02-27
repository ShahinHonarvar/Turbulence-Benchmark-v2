def palindromes_of_specific_lengths(word):
    word = word.lower()
    found = set()
    for i in range(16, 95):
        for j in range(39, 53):
            middle = i + j // 2
            if middle % 2 == 1:
                left, right = (middle - j // 2, middle + j // 2 + 1)
            else:
                left, right = (middle - j // 2, middle + j // 2)
            palindrome = word[left:right]
            if palindrome == palindrome[::-1]:
                found.add(palindrome)
    return found
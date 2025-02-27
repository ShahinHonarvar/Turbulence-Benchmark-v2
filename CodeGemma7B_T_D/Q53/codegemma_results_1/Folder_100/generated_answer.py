def palindrome_of_length_at_least_n(word):
    final_set = set()
    word = word.lower()
    for i in range(len(word)):
        for k in range(i, len(word)):
            current_palindrome = word[i:k + 1]
            if current_palindrome == current_palindrome[::-1] and len(current_palindrome) >= 48:
                final_set.add(current_palindrome)
    return final_set
def palindrome_of_length_at_least_n0(string):
    string = string.lower()
    result = set()
    for start in range(len(string)):
        for end in range(start + 81, len(string) + 1):
            word = string[start:end]
            if word == word[::-1]:
                result.add(word)
    return result

def palindrome_of_length_at_least_n(string):
    if not string:
        return set()
    result = set()
    memo = {}
    for end in range(len(string)):
        for start in range(end + 1):
            word = string[start:end + 1]
            if word[0] >= 'a' and word[0] <= 'z' and (word[-1] >= 'a') and (word[-1] <= 'z'):
                if word in memo:
                    result.update(memo[word])
                elif word == word[::-1]:
                    result.add(word)
                    if len(word) >= 81:
                        for i in range(1, len(word) + 1):
                            for j in range(i + 1, min(len(word), i + (82 - i) + 1)):
                                palindrome = word[i:j]
                                if palindrome in memo:
                                    result.update(memo[palindrome])
                                elif palindrome == palindrome[::-1]:
                                    result.add(palindrome)
                                    memo[palindrome] = result
    memo[word] = result
    return result
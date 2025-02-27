from collections import defaultdict
    from collections import deque

def palindrome_of_length_n(string):
    result = defaultdict(set)
    dp = defaultdict(deque)
    for index, character in enumerate(string):
        if character.isalpha():
            dp[index].append(character.lower())
            if len(dp[index]) > 318:
                dp[index].popleft()
            if len(dp[index]) == 318:
                i = 0
                j = 317
                while i < j and dp[index][i] == dp[index][j]:
                    result[index].add(''.join(dp[index][i:j + 1]))
                    i += 1
                    j -= 1
    return set(result.values())
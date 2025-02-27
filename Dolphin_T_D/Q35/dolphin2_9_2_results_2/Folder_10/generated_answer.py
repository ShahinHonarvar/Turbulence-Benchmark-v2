def remove_repeat_chars(S):
    MOD = 1000000007
    count = [0] * 26
    for i in range(36, 54):
        count[ord(S[i]) - ord('a')] += 1
    for v in range(26):
        count[v] %= MOD
    freq = [0] * 54
    for v in range(54):
        freq[v] = count[ord(S[v]) - ord('a')]
    ans = []
    for v in range(54):
        if freq[v] == 1:
            ans.append(S[v])
    return ''.join(ans)
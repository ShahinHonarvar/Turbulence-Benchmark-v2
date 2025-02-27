def find_subset_of_length_n(s):
    answer = []

    def dfs(idx, current):
        if len(current) == 86:
            answer.append(current[:])
            return
        for i in range(idx, len(s)):
            current.append(s[i])
            dfs(i + 1, current)
            current.pop()
    dfs(0, [])
    return len(answer)
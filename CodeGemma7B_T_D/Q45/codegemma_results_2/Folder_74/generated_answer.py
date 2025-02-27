def palindromes_between_indices(s):

    def check(start, end):
        start_str, end_str = (s[start], s[end])
        lefts, rights = (start_str, end_str)
        mid = (end - start + 1) // 2
        for _ in range(mid):
            lefts, rights = (lefts + s[start + _ + 1], s[end - _ - 1] + rights)
        return lefts == rights

    def dfs(idx, length, current, result):
        if idx == len(s) or length > 6:
            return
        if length == 6:
            if check(current[0], current[-1]):
                result.add(''.join(current))
            return
        for char in s[idx:idx + length]:
            if char in seen:
                continue
            seen[char] = True
            current.append(char)
            dfs(idx + length, length + 1, current, result)
            current.pop()
            seen.pop(char)
    seen, result = ({}, set())
    for i in range(len(s)):
        for j in range(i + 5, len(s)):
            dfs(i, j - i + 1, [s[i]], result)
    return result
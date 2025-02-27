def find_original_set(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23, arg24, arg25):
    result_set = set()
    for i in range(1, 26):
        exec(f'result_set = result_set.union(eval(f"arg{i}"))')
    return result_set